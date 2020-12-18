from harborclient_light import harborclient

def setup_harbor_client():
    harbor_host = "harbor.container-registry.com"
    harbor_user = "admin_user"
    harbor_pass = "admin_pass"
    return harborclient.HarborClient(
            harbor_host, harbor_user, harbor_pass)

harbor_client = setup_harbor_client()

def create_harbor_user_from_customer(customer):
    if not self.customer_email:
        raise ValueError("Couldn't create harbor user for customer %s - the object doesn't have the email set" % (customer.id))
    generated_password = ''.join(
            random.sample(string.ascii_letters + string.digits, 16)),
    user = harbor_client.create_user(
            # use email as username for simplicity
            self_customer_email,
            self.customer_email,
            generated_password,
            # don't set a real name
            "",
            # don't set a comment
            "")
    # send email?
    return user

def provision_harbor_permissions_for_customer(customer):
    project_name = "software_product_repo"
    # add permissions
    return True

def remove_product_access_for_customer(customer):
    # remove product access
    return True
