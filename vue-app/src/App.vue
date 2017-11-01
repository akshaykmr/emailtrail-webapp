<template>
  <div id="analyse-email">
    <form action="" id ="email-form">
      <textarea class="glowing-border" id="email-source" rows="15" v-model="email"
      placeholder="Paste email headers here and then click analyse 🔍">
      </textarea>
    </form>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'app',
  components: {
    HelloWorld,
  },
  data() {
    return {
      email: '',
    };
  },
};
</script>

<style lang="scss">
#email-form {
  text-align: center;
}
#email-source {
  padding: 5px;
  font-size: 20px;
  font-family: "Cutive Mono";
  width: 90%;
  max-width: 780px;
  margin: 20px;
  margin-top: 10px;
}
.glowing-border {
    border: 2px solid #dadada;
    border-radius: 3px;
}

.glowing-border:focus {
    outline: none;
    border-color: #c4f2eb;
    box-shadow: 0 0 10px #c4f2eb;
}
</style>
