package main

import (
	"math"
	"testing"
)

func testSqrt(t *testing.T) {
	actual := Sqrt(100)
	expected := 10.0
	if actual != expected {
		t.Errorf("Expected Float(%f) is not same as"+
			" actual Float(%f)", expected, actual)
	}
}

func testPic(t *testing.T) {
	pic := Pic(10, 10)
	for i := range make([]int, 10) {
		for j := range make([]int, 10) {
			expected := math.Pow(float64(i), float64(j))
			actual := pic[i][j]
			if actual != uint8(expected) {
				t.Errorf("Expected uint8(%v) is not same as"+
					" actual uint8(%v)", expected, actual)
			}
		}
	}
}
