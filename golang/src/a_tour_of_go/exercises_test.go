package main

import (
	"testing"
)

func testSqrt(t *testing.T) {
	actualFloat := Sqrt(100)
	expectedFloat := 10.0
	if actualFloat != expectedFloat {
		t.Errorf("Expected Float(%f) is not same as"+
			" actual Float (%f)", expectedFloat, actualFloat)
	}
}
