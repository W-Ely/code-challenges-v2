package main

import (
	"bytes"
	"testing"
)

func testHello(t *testing.T) {
	var output bytes.Buffer
	Hello(&output)
	expected := "Hello, 世界"
	if expected != output.String() {
		t.Errorf("got %s but expected %s", output.String(), expected)
	}
}
