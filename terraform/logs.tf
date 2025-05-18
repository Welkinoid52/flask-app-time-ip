resource "aws_cloudwatch_log_group" "flasky2" {
  name              = "/ecs/flasky2"
  retention_in_days = 7
}