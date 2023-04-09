package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"math"
	"reflect"
	"strings"
	"testing"
)

func TestSqrt(t *testing.T) {
	actual := Sqrt(100)
	expected := 10.0
	if actual != expected {
		t.Errorf("Expected Float (%f) is not same as"+
			" actual Float (%f)", expected, actual)
	}
}

func TestPic(t *testing.T) {
	pic := Pic(10, 10)
	for i := range make([]int, 10) {
		for j := range make([]int, 10) {
			expected := math.Pow(float64(i), float64(j))
			actual := pic[i][j]
			if actual != uint8(expected) {
				t.Errorf("Expected uint8 (%v) is not same as"+
					" actual uint8 (%v)", expected, actual)
			}
		}
	}
}

func TestWordCount(t *testing.T) {
	s := "a b b c c c"
	actual := WordCount(s)
	expected := map[string]int{"a": 1, "b": 2, "c": 3}
	eq := reflect.DeepEqual(actual, expected)
	if !(eq) {
		t.Errorf("Expected map[string]int (%v) is not same as"+
			" actual map[string]int (%v)", expected, actual)
	}
}

func TestFibonacci(t *testing.T) {
	f := Fibonacci()
	for _, v := range []int{0, 1, 1, 2, 3, 5, 8, 13, 21, 34} {
		actual := f()
		expected := v
		if actual != expected {
			t.Errorf("Expected int (%v) is not same as"+
				" actual int (%v)", expected, actual)
		}
	}
}

func TestIPAddrStringer(t *testing.T) {
	ip := IPAddr{1, 1, 1, 1}
	var output bytes.Buffer
	fmt.Fprintf(&output, "%v", ip)
	expected := "1.1.1.1"
	if expected != output.String() {
		t.Errorf("got %s but expected %s", output.String(), expected)
	}
}

func TestSqrt2(t *testing.T) {
	actual, err := Sqrt2(100)
	expected := 10.0
	if err != nil {
		t.Errorf("Expected Float (%f) but got Error (%v)", expected, err)
	}
	if actual != expected {
		t.Errorf("Expected Float (%f) is not same as"+
			" actual Float (%f)", expected, actual)
	}
	actual, err = Sqrt2(-100)
	expected_err := ErrNegativeSqrt(-100)
	if err == nil {
		t.Errorf("Expected Error (%v) but got error %v", expected_err, actual)
	}
}

func TestMyReader(t *testing.T) {
	b := make([]byte, 8)
	r := MyReader{}
	i := 0
	for i <= 24 {
		n, _ := r.Read(b)
		for j, v := range b[:n] {
			if v != 'A' {
				t.Errorf("Expected 'A' but got error %v", v)
			}
			i += j
		}
	}
}

func TestRot13Reader(t *testing.T) {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	expected := "You cracked the code!"
	r := Rot13Reader{s}
	actual, _ := ioutil.ReadAll(&r)
	if string(actual) != expected {
		t.Errorf("got %s but expected %s", actual, expected)
	}
}
