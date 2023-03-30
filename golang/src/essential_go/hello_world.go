package main

import (
	"fmt"
	"io"
	"os"
)

func Hello(w io.Writer) {
	fmt.Fprintf(w, "Hello, 世界")
}

func main() {
	Hello(os.Stdout)
}
