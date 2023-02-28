package main

import (
	"bytes"
	"fmt"
	"math"
	"reflect"
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
	expected_err := "cannot Sqrt negative number: -100"
	if err == nil {
		t.Errorf("Expected Error (%v) but got error %v", expected_err, actual)
	}
}
