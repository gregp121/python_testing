package main

import (
	"fmt"
	"math"
)

// Go does NOT have classes. But you can define methods on types.
// A method = function with special reciever argument that appears in its own argument list between the func and method name
type Vertex struct {
	X, Y float64
}


// Below, our method is expecting a Vertex struct
func (v Vertex) Abs() float64 {  // Here, the Abs method has a reciever of the ype Vertex struct. Not: both are float64
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v: Vertex{3, 4} // We define Vertex here
	fmt.Println(v.Abs()) // Then we invoke our method on the struct
}

// A method is just a function with a reciever argument
// Identical to the results above is:
func Abs(v Vertex) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v: Vertex{3, 4} // We define Vertex here
	fmt.Println(Abs(v)) // Then we invoke our method on the struct
}
// Both return 5