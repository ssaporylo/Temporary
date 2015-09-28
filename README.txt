Credentials to API:
   - username: root
   - password: Install_new!

Before run API query need to login

Request API
Example:
    http://127.0.0.1:8000/books/line-vindernovelle-i-krimidysten/?watermark=12wr78d8f9f6f9f8c5
    details:
    line-vindernovelle-i-krimidysten - this is book name
    12wr78d8f9f6f9f8c5 - watermark value

    After request this source ("http://127.0.0.1:8000/books/line-vindernovelle-i-krimidysten/?watermark=12wr78d8f9f6f9f8c5"):
    1. Retrieve the file from the input file URL ("line-vindernovelle-i-krimidysten")
	2. Unzip the ePub file
    3. Find the META-INF/container.xml file and open that
    4. Add the “order hash” (value watermark in url) and a timestamp to a comment in the container.xml XML file
    5. Save the file and ZIP the contents as the original name of the epub file and deliver it to the user

 