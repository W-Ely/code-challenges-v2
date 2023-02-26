package main

import (
	"math"
	"reflect"
	"testing"
)

func testSqrt(t *testing.T) {
	actual := Sqrt(100)
	expected := 10.0
	if actual != expected {
		t.Errorf("Expected Float (%f) is not same as"+
			" actual Float (%f)", expected, actual)
	}
}

func testPic(t *testing.T) {
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

func testWordCount(t *testing.T) {
	s := "a b b c c c"
	actual := WordCount(s)
	expected := map[string]int{"a": 1, "b": 2, "c": 3}
	eq := reflect.DeepEqual(actual, expected)
	if !(eq) {
		t.Errorf("Expected map[string]int (%v) is not same as"+
			" actual map[string]int (%v)", expected, actual)
	}
}

func testFibonacci(t *testing.T) {
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
