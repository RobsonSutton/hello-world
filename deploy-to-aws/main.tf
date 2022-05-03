provider "aws" {
  region = "eu-west-2"
}

resource "aws_instance" "ec2_instance" {  # https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance
  ami           = "ami-0710bbbc1e526fa78" # AWS Marketplace to find AMI's - Ubuntu 18.04
  instance_type = "t2.micro"              # AWS Free Tier EC2
  key_name      = "hello-world"

  tags = {
    "Name" = "hello-world" # Add Name to EC2 instance
  }
}
