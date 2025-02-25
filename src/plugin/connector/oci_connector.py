import oci
from spaceone.core.connector import BaseConnector

def get_config(secret_data):
    
    config = {
        "user": secret_data["user"],
        "fingerprint": secret_data["fingerprint"],
        "key_file": secret_data["key_file"],
        "tenancy": secret_data["tenancy"],
        "region": secret_data["region"],
        "pass_phrase": secret_data.get("pass_phrase")
    }
    return config

class OCIConnector(BaseConnector):
    @staticmethod
    def get_account_id(secret_data):
        config = get_config(secret_data)
        from oci.signer import Signer
        signer = Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config["key_file"],
            pass_phrase=config.get("pass_phrase")
        )
        # IdentityClient 생성 시, config는 빈 dict로 두고 signer를 전달합니다.
        identity_client = oci.identity.IdentityClient(config={}, signer=signer)
        tenancy = identity_client.get_tenancy(config["tenancy"]).data
        return tenancy.id