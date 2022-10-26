import boto3

#https://boto3.amazonaws.com/v1/documentation/api/latest/guide/cw-example-creating-alarms.html

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Create alarm
cloudwatch.put_metric_alarm(
    AlarmName='Web_Server_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=False,
    AlarmDescription='Alarm when server CPU exceeds 70%',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'INSTANCE_ID'
        },
    ],
    Unit='Seconds'
)