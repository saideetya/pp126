getPermissionAsync = async () => {
   if  (Platform.OS !== "web") {
      const { status } = await Permissions.askasync(Permissions.CAMERA_ROLL);
      if (status !== "granted") {
          alert("Sorry, we need camera roll permissionsto make this work!");
      }
   }
};

uploadImage = async (uri) => {
   const data = new FormData() ;
   let filename = uri.split("/")[uri.split("/").length - 1]
   let type = `image/${uri.split('.')[uri.split('.').length - 1]}`
   const fileToUpload = {
      uri: uri,
      name: filename,
      type: type,
   };
   data.append("digit", fileToUpload);
   fetch("htpps://f292a3137990.ngrok.io/predict-digit", {
      method: "POST",
      body: data,
      headers: {
         "content-type": "multipart/from-data",
      }
   })
      .then((response) => response.json())
      .then((result) => {
         "console.log("Success:", result);
      })
      .catch((error) => {
         console.error("Error:", error);
      });

   }