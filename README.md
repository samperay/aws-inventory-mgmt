## Cloud Management

# Summay

This project would display the inventory of the AWS instances, if you are working on large environments. 
we are using python django application to further build this project. 

# Requirements

automated scripts are being placed in central repository and would download an latest .csv file with complete details of inventory.
This project shall take that inventory file as an input and shall be displaying in web framework so that anyone don't have to download their copies.

Majors from .csv which we need to focus on

```
instance_id
instance_type
ami_id
instance_status
availability_zone
public_ip
private_ip
instance_keypair
dns_public
dns_private
```

CSV file was loaded using python script which copies data in dbsqlite, the csv file has to be in same location as *manage.py* as it would require djano management to load to DB

```
$ python manage.py load_csv
Creating Inventory data
Loading Inventory data for Inventory available for AWS
$
```
If there are still errors while migrating, you can * rm -rf migrations/ and then try loading the data.



