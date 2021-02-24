package main

import (
	"context"

	"github.com/aws/aws-sdk-go-v2/config"
)

func main() {
	config.LoadDefaultConfig(context.Background())
}
