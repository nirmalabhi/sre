import boto3

access_key = "access key"
secret_key = "secret key"
ec2_regions = ['us-east-1']

for region in ec2_regions:
	conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name='us-east-1')
	instances = conn.instances.filter()
	list1 = []
	for instance in instances:
		if (instance.state["Name"] == "running" and instance.instance_type == "m5.large"):
			for instance_name in instance.tags:
				instance_name_value = instance_name["Value"]
				print_items = "Region: {0}\nName: {1}\nInstance ID: {2}\nPublic IPv4: {3}\nInstance Type: {4} \n".format(region, instance_name_value, instance.id, instance.public_ip_address, instance.instance_type)
				print(print_items)
