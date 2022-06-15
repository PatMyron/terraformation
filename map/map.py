import requests
cfTypes = requests.get('https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json').json()['ResourceTypes'].keys()
tfTypes = requests.get('https://raw.githubusercontent.com/PatMyron/terraformation/create-pull-request/patch/schemas/tf/schema.json').json()['provider_schemas']['registry.terraform.io/hashicorp/awscc']['resource_schemas'].keys()


def mapTypes(cfTypes, tfTypes):
  cfMap = {}
  for cfType in cfTypes:
    cfMap[cfType.replace('_', '').replace(':', '').lower()] = cfType
  for tfType in tfTypes:
    try:
      print(tfType, cfMap[tfType.replace('_', '').replace(':', '').lower().replace('awscc', 'aws')])
    except:
      pass

mapTypes(cfTypes, tfTypes)
