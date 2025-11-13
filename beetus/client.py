from pfun_cma_model_client import openapi_client
from pfun_cma_model_client.openapi_client.rest import ApiException
from pprint import pprint


class BeetusClient:
    def __init__(self):
        # Defining the host is optional and defaults to https://pfun-cma-model-446025415469.us-central1.run.app
        # See configuration.py for a list of all supported configuration parameters.
        self.configuration = openapi_client.Configuration(
            host="https://pfun-cma-model-446025415469.us-central1.run.app"
        )

    def __enter__(self):
        # Enter a context with an instance of the API client
        with openapi_client.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.DefaultApi(api_client)
            return api_instance

    def __exit__(self, exc_type, exc_value, traceback):
        # Exit the context and close the API client
        pass


def main():
    print("Testing beetus openapi client...")
    client_instance = BeetusClient()

    def test_default_params_with_ctx(client_instance=client_instance):
        try:
            # Default Params
            api_response = client_instance.default_params_params_default_get()
            print("The response of DefaultApi->default_params_params_default_get:\n")
            pprint(api_response)
        except ApiException as e:
            print(
                "Exception when calling DefaultApi->default_params_params_default_get: %s\n" % e)

    with BeetusClient() as client_instance:
        test_default_params_with_ctx(client_instance)

    print("Finished testing beetus openapi client.")


if __name__ == '__main__':
    main()
