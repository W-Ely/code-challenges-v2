package main

import (
	"fmt"
	"io"
	"os"
)

func Hello(w io.Writer) {
	fmt.Println(w, "Hello, 世界")
}

func main() {
	Hello(os.Stdout)
}
