
json_data = {
      "Reservations": [
    {
      "Groups": [],
      "Instances": [
        {
          "AmiLaunchIndex": 0,
          "ImageId": "ami-05841cb985d4a9aa7",
          "InstanceId": "i-03fd3ec7a44e04e2f",
          "InstanceType": "m5.large",
          "KeyName": "dev-ecs-instance",
          "LaunchTime": "2019-11-25 06:18:47+00:00",
          "Monitoring": {
            "State": "enabled"
          },
          "Placement": {
            "AvailabilityZone": "ap-southeast-2a",
            "GroupName": "",
            "Tenancy": "default"
          },
          "PrivateDnsName": "ip-10-56-16-37.ap-southeast-2.compute.internal",
          "PrivateIpAddress": "10.56.16.37",
          "ProductCodes": [],
          "PublicDnsName": "",
          "State": {
            "Code": 16,
            "Name": "running"
          },
          "StateTransitionReason": "",
          "SubnetId": "subnet-0908e76bc4624de69",
          "VpcId": "vpc-05f30b406d00478b7",
          "Architecture": "x86_64",
          "BlockDeviceMappings": [
            {
              "DeviceName": "/dev/xvda",
              "Ebs": {
                "AttachTime": "2019-11-25 06:18:48+00:00",
                "DeleteOnTermination": True,
                "Status": "attached",
                "VolumeId": "vol-0cceda124501f5426"
              }
            },
            {
              "DeviceName": "/dev/xvdcz",
              "Ebs": {
                "AttachTime": "2019-11-25 06:18:48+00:00",
                "DeleteOnTermination": True,
                "Status": "attached",
                "VolumeId": "vol-0aa7fa20d1a937ebc"
              }
            }
          ],
          "ClientToken": "2095ba84-d987-d569-7e87-533d8c0f1f01_subnet-0908e76bc4624de69_1",
          "EbsOptimized": False,
          "EnaSupport": True,
          "Hypervisor": "xen",
          "IamInstanceProfile": {
            "Arn": "arn:aws:iam::221843028483:instance-profile/cde-ecscluster-dev-ECSInstanceProfile-13XHY5YSJ0E1K",
            "Id": "AIPATHJW77IB7TDQA5AL3"
          },
          "NetworkInterfaces": [
            {
              "Attachment": {
                "AttachTime": "2019-11-25 06:18:47+00:00",
                "AttachmentId": "eni-attach-0cc0ffd8e3556d8c8",
                "DeleteOnTermination": True,
                "DeviceIndex": 0,
                "Status": "attached"
              },
              "Description": "",
              "Groups": [
                {
                  "GroupName": "cde-securitygroups-dev-ECSCluster-TO0QRXSJH9CJ",
                  "GroupId": "sg-0427ccc046013cae0"
                }
              ],
              "Ipv6Addresses": [],
              "MacAddress": "02:fc:ef:f8:1c:90",
              "NetworkInterfaceId": "eni-09a097a169155c402",
              "OwnerId": "221843028483",
              "PrivateDnsName": "ip-10-56-16-37.ap-southeast-2.compute.internal",
              "PrivateIpAddress": "10.56.16.37",
              "PrivateIpAddresses": [
                {
                  "Primary": True,
                  "PrivateDnsName": "ip-10-56-16-37.ap-southeast-2.compute.internal",
                  "PrivateIpAddress": "10.56.16.37"
                }
              ],
              "SourceDestCheck": True,
              "Status": "in-use",
              "SubnetId": "subnet-0908e76bc4624de69",
              "VpcId": "vpc-05f30b406d00478b7",
              "InterfaceType": "interface"
            },
            {
              "Attachment": {
                "AttachTime": "2019-11-25 06:20:16+00:00",
                "AttachmentId": "eni-attach-0f619b30868f75ebf",
                "DeleteOnTermination": False,
                "DeviceIndex": 1,
                "Status": "attached"
              },
              "Description": "arn:aws:ecs:ap-southeast-2:221843028483:attachment/c87bd27e-87e4-46aa-8e83-b5972adbb38e",
              "Groups": [
                {
                  "GroupName": "default",
                  "GroupId": "sg-07981ceb8b5573e4e"
                }
              ],
              "Ipv6Addresses": [],
              "MacAddress": "02:ac:8d:e4:0e:0e",
              "NetworkInterfaceId": "eni-024fc05452887fd0a",
              "OwnerId": "221843028483",
              "PrivateDnsName": "ip-10-56-16-165.ap-southeast-2.compute.internal",
              "PrivateIpAddress": "10.56.16.165",
              "PrivateIpAddresses": [
                {
                  "Primary": True,
                  "PrivateDnsName": "ip-10-56-16-165.ap-southeast-2.compute.internal",
                  "PrivateIpAddress": "10.56.16.165"
                }
              ],
              "SourceDestCheck": True,
              "Status": "in-use",
              "SubnetId": "subnet-0908e76bc4624de69",
              "VpcId": "vpc-05f30b406d00478b7",
              "InterfaceType": "trunk"
            }
          ],
          "RootDeviceName": "/dev/xvda",
          "RootDeviceType": "ebs",
          "SecurityGroups": [
            {
              "GroupName": "cde-securitygroups-dev-ECSCluster-TO0QRXSJH9CJ",
              "GroupId": "sg-0427ccc046013cae0"
            }
          ],
          "SourceDestCheck": True,
          "Tags": [
            {
              "Key": "aws:autoscaling:groupName",
              "Value": "cde-ecscluster-dev-ECSAutoScalingGroup-12GLVGAUMZRAV"
            },
            {
              "Key": "aws:cloudformation:logical-id",
              "Value": "ECSAutoScalingGroup"
            },
            {
              "Key": "aws:cloudformation:stack-name",
              "Value": "cde-ecscluster-dev"
            },
            {
              "Key": "aws:cloudformation:stack-id",
              "Value": "arn:aws:cloudformation:ap-southeast-2:221843028483:stack/cde-ecscluster-dev/3c047770-a452-11e9-a28e-028d024c9854"
            },
            {
              "Key": "IsECSHost",
              "Value": "True"
            },
            {
              "Key": "Name",
              "Value": "dev ECS host"
            },
            {
              "Key": "Environment",
              "Value": "dev"
            }
          ],
          "VirtualizationType": "hvm",
          "CpuOptions": {
            "CoreCount": 1,
            "ThreadsPerCore": 2
          },
          "CapacityReservationSpecification": {
            "CapacityReservationPreference": "open"
          },
          "HibernationOptions": {
            "Configured": False
          }
        }
      ],
      "OwnerId": "221843028483",
      "RequesterId": "081202882002",
      "ReservationId": "r-0fa2934281c60011a"
    }
      ],
      "OwnerId": "221843028483",
      "RequesterId": "081202882002",
      "ReservationId": "r-06fd0649b9c3631b6"
    }


def find_without_skip(root_dict, pattern):

    def lookup_dict(new_root_dict, new_pattern):
        k = new_pattern
        v = new_root_dict.get(new_pattern)
        if not v:
            for nk, nv in new_root_dict.items():
                if type(nv) == list:
                    lookup_list(nv, new_pattern)
                elif type(nv) == dict:
                    lookup_dict(nv, new_pattern)
            return
        if not result.get(new_pattern):
            result[new_pattern] = v
        else:
            if type(result[new_pattern]) == list:
                result[new_pattern].append(v)
            else:
                temp = result[new_pattern]
                result[new_pattern] = []
                result[new_pattern].append(temp)
                result[new_pattern].append(v)

    def lookup_list(new_root_list, new_pattern):
        for element in new_root_list:
            if type(element) == dict:
                lookup_dict(element, new_pattern)

    lookup_keys = pattern.split("_")
    lookup_keys.reverse()
    result = {}.fromkeys(lookup_keys)
    lookup_key = lookup_keys.pop()

    while lookup_keys:
        if result[lookup_key]:
            lookup_key = lookup_keys.pop()
        print("\nLookup Key:: ", lookup_key, "\n")
        if type(root_dict) == dict:
            lookup_dict(root_dict, lookup_key)
        elif type(root_dict) == list:
            lookup_list(root_dict, lookup_key)
        else:
            print(result[lookup_key])

        root_dict = result[lookup_key]

    #print(result)
    return result


pattern = "Reservations_Instances_InstanceId"
result = find_without_skip(json_data, pattern)
print("\nExpected --> ", result["InstanceId"])

pattern = "Reservations_SecurityGroups"
result = find_without_skip(json_data, pattern)
print("\nExpected --> ", result["SecurityGroups"])
