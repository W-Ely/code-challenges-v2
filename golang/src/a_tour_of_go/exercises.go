package main

import (
	"fmt"
	"io"
	"math"
	"os"
	"strings"

	"golang.org/x/tour/pic"
	"golang.org/x/tour/reader"
	"golang.org/x/tour/wc"
)

/* Exercise: Loops and Functions

As a way to play with functions and loops, let's implement a
square root function: given a number x, we want to find the
number z for which z² is most nearly x.

Computers typically compute the square root of x using a loop.
Starting with some guess z, we can adjust z based on how close z²
is to x, producing a better guess:

z -= (z*z - x) / (2*z)

Repeating this adjustment makes the guess better and better
until we reach an answer that is as close to the actual square
root as can be.

Implement this in the func Sqrt provided. A decent starting
guess for z is 1, no matter what the input. To begin with, repeat
the calculation 10 times and print each z along the way. See how
close you get to the answer for various values of x (1, 2, 3, ...)
and how quickly the guess improves.

Hint: To declare and initialize a floating point value, give it
floating point syntax or use a conversion:

z := 1.0
z := float64(1)
Next, change the loop condition to stop once the value has stopped
changing (or only changes by a very small amount). See if that's
more or fewer than 10 iterations. Try other initial guesses for z,
like x, or x/2. How close are your function's results to the
math.Sqrt in the standard library?

(Note: If you are interested in the details of the algorithm, the
z² − x above is how far away z² is from where it needs to be (x),
and the division by 2z is the derivative of z², to scale how much we
adjust z by how quickly z² is changing. This general approach is called
Newton's method. It works well for many functions but especially well
for square root.)

- https://go.dev/flowcontrol/8
*/

func Sqrt(x float64) float64 {
	z := 1.0
	maxDiff := 0.0000000001
	for !(math.Abs(x-z*z) <= maxDiff) {
		z -= (z*z - x) / (2 * z)
	}
	return z
}

/* Exercise: Slices
Implement Pic. It should return a slice of length dy, each element of
which is a slice of dx 8-bit unsigned integers. When you run the program,
it will display your picture, interpreting the integers as grayscale
(well, bluescale) values.

The choice of image is up to you. Interesting functions include
(x+y)/2, x*y, and x^y.

(You need to use a loop to allocate each []uint8 inside the [][]uint8.)

(Use uint8(intValue) to convert between types.)
*/

func Pic(dx, dy int) [][]uint8 {
	s := make([][]uint8, dy)
	for i := range s {
		s[i] = make([]uint8, dx)
		for j := range s[i] {
			s[i][j] = uint8(math.Pow(float64(i), float64(j)))
		}
	}
	return s
}

/*
	Exercise: Maps

Implement WordCount. It should return a map of the counts of each
“word” in the string s. The wc.Test function runs a test suite against
the provided function and prints success or failure.

You might find strings.Fields helpful.
*/
func WordCount(s string) map[string]int {
	wc := make(map[string]int)
	ws := strings.Fields(s)
	for _, w := range ws {
		wc[w] += 1
	}

	return wc
}

/* Exercise: Fibonacci closure
Let's have some fun with functions.

Implement a fibonacci function that returns a function (a closure) that
returns successive fibonacci numbers (0, 1, 1, 2, 3, 5, ...).
*/

func Fibonacci() func() int {
	fib := 0
	next := 1
	return func() int {
		result := fib
		fib, next = next, fib+next
		return result
	}
}

/* Exercise: Stringers

Make the IPAddr type implement fmt.Stringer to print the address as a dotted quad.

For instance, IPAddr{1, 2, 3, 4} should print as "1.2.3.4".
*/

type IPAddr [4]byte

func (ip IPAddr) String() string {
	return fmt.Sprintf("%d.%d.%d.%d", ip[0], ip[1], ip[2], ip[3])
}

/*
	Exercise: Errors

Copy your Sqrt function from the earlier exercise and modify it to return
an error value.

Sqrt should return a non-nil error value when given a negative number, as
it doesn't support complex numbers.

# Create a new type

type ErrNegativeSqrt float64
and make it an error by giving it a

func (e ErrNegativeSqrt) Error() string
method such that ErrNegativeSqrt(-2).Error() returns "cannot Sqrt negative
number: -2".

Note: A call to fmt.Sprint(e) inside the Error method will send the program
into an infinite loop. You can avoid this by converting e
first: fmt.Sprint(float64(e)). Why?

Change your Sqrt function to return an ErrNegativeSqrt value when given a
negative number.
*/
type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("cannot Sqrt negative number: %v", fmt.Sprint(float64(e)))
}

func Sqrt2(x float64) (float64, error) {
	if x < 0 {
		return 0, ErrNegativeSqrt(x)
	}
	z := 1.0
	maxDiff := 0.0000000001
	for !(math.Abs(x-z*z) <= maxDiff) {
		z -= (z*z - x) / (2 * z)
	}
	return z, nil
}

/* Exercise: Readers
Implement a Reader type that emits an infinite stream of the ASCII character 'A'.
*/

type MyReader struct{}

// TODO: Add a Read([]byte) (int, error) method to MyReader.

func (r MyReader) Read(b []byte) (int, error) {
	count := 0
	for i := range b {
		b[i] = 65
		count += 1
	}
	return count, nil
}

/* Exercise: rot13Reader
A common pattern is an io.Reader that wraps another io.Reader, modifying
the stream in some way.

For example, the gzip.NewReader function takes an io.Reader (a stream of
	compressed data) and returns a *gzip.Reader that also implements io.Reader
	(a stream of the decompressed data).

Implement a rot13Reader that implements io.Reader and reads from an io.Reader,
modifying the stream by applying the rot13 substitution cipher to all
alphabetical characters.

The rot13Reader type is provided for you. Make it an io.Reader by implementing
its Read method.
*/

type Rot13Reader struct {
	r io.Reader
}

func (r13 *Rot13Reader) Read(b []byte) (int, error) {
	n, err := r13.r.Read(b)
	for i := 0; i <= n; i++ {
		if (b[i] >= 65 && b[i] <= 77) || (b[i] >= 97 && b[i] <= 109) {
			b[i] = b[i] + 13
		} else if (b[i] >= 78 && b[i] <= 90) || (b[i] >= 110 && b[i] <= 122) {
			b[i] = b[i] - 13
		}
	}
	return n, err
}

func main() {
	fmt.Println(Sqrt(8000))

	pic.Show(Pic)

	wc.Test(WordCount)

	f := Fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}

	hosts := map[string]IPAddr{
		"loopback":  {127, 0, 0, 1},
		"googleDNS": {8, 8, 8, 8},
	}
	for name, ip := range hosts {
		fmt.Printf("%v: %v\n", name, ip)
	}

	fmt.Println(Sqrt2(2))
	fmt.Println(Sqrt2(-2))

	reader.Validate(MyReader{})

	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := Rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
