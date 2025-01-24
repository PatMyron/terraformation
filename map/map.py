import requests
cfTypes = requests.get('https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json').json()['ResourceTypes'].keys()
tfTypes = requests.get('https://raw.githubusercontent.com/PatMyron/terraformation/create-pull-request/patch/schemas/tf/schema.json').json()['provider_schemas']['registry.terraform.io/hashicorp/aws']['resource_schemas'].keys()


def mapTypes(cfTypes, tfTypes):
  cfMap = {}
  for cfType in cfTypes:
    cfMap[cfType.replace('_', '').replace(':', '').lower()] = cfType
  for tfType in tfTypes:
    try:
      print(tfType, cfMap[tfType.replace('aws_bedrockagent_', 'aws_bedrock_').replace('aws_ssoadmin_', 'aws_sso_').replace('aws_sesv2_', 'aws_ses_').replace('aws_cloudwatch_log_', 'aws_logs_').replace('aws_cloudwatch_event_', 'aws_events_').replace('aws_db_', 'aws_rds_db_').replace('aws_vpc_', 'aws_ec2_').replace('_', '').replace(':', '').lower()])
    except:
      pass

mapTypes(cfTypes, tfTypes)
