<template>
<body style="background-color: #BBAAB8; height: 100%; width: 100%;">  
<div>
  <img src="@/assets/Hospital.jpg" style="height: 50%; width: 50%;" />
  <h1>Bienvenido a Homecare</h1>
</div>
</body>
</template>
  <script>
  export default {
    name: "Home",
    data: function () {
      return {
        username: localStorage.getItem("username") || "none",
      };
    },
  };
  </script>
  <style>
  body {

  }
  .greetings h1 {
    font-size: 50px;
    color: #283747;
  }
  .greetings span {
    color: crimson;
    font-weight: bold;
  }
  </style>