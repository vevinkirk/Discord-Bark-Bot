import boto3

client = boto3.client('ec2')

def get_latest_debian_ami(cpu):
     response = client.describe_images(
          Filters=[
               {
                    'Name': 'architecture',
                    'Values' : [
                         cpu
                    ],
                    'Name': 'name',
                    'Values': [
                         'debian-10*'
                    ]
               },
          ],
          Owners=[
               '136693071363'
          ]
     )
     print(response)

print(get_latest_debian_ami)

images = get_latest_debian_ami('x86_64')

print(images)