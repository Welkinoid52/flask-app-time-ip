provider "aws" {
  region = var.region
}

# This file primarily serves as the entry point that ties all modules together
# All resources are organized in their respective files