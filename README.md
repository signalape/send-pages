## AWS Lambda Function to call DAPNET API

*This lambda function calls the DAPNET API to send a page. It supports multiple destination callsigns and transmitter groups.*

### Usage

The function expects three environment variables under Configuration > Environment Variables

DAPNET_AUTH_HEADER 

Basic **{Base64 encoded username and password}**

DAPNET_HOST

hampager.de                                   

DAPNET_PATH

/api/calls

Replace **{Base64 encoded username and password}** with the appropriate value based on the user credentials.
