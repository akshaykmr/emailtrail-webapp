<template>
  <div id="analyse-email">
    <div id ="email-form">
      <textarea class="glowing-border" id="email-source" rows="15" v-model="email"
      placeholder="Paste email headers here and then click analyse 🔍">
      </textarea>
      <div class="submit-button" v-on:click="analyseEmail">Analyse</div>
      <div class="analysis">
        <div class="loader" v-if="loading">
        </div>
        <div class="error-message" v-if="error">
          {{errorMessage}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'AnalyseEmail',
  data() {
    return {
      email: '',
      analysis: {},
      loading: false,
      error: false,
      errorMessage: 'Something went wrong... Check your input or try again, else reach me on twitter: @uberakshay',
    };
  },
  methods: {
    analyseEmail: function () {
      this.loading = true;
      // const email = this.email;
      axios.post('/api/v1/analyse', this.email)
        .then((response) => {
          this.analysis = response.data.analysis
          this.error = '';
          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
          this.error = true;
          this.loading = false;
        });
    },
  },
};
</script>

<style lang="scss">
#email-form {
  text-align: center;
  padding-bottom: 40px;

  .submit-button {
    cursor: pointer;
    user-select: none;
    -webkit-border-radius: 5;
    -moz-border-radius: 5;
    border-radius: 5px;
    color: #ffffff;
    font-size: 20px;
    background: #799e8a;
    padding: 10px 20px 10px 20px;
    width: 120px;
    margin: 0 auto;

    &.disabled {
      cursor: not-allowed;
    }

    &:hover {
      background: #6d8d7c;
    }

    &:active {
      background: #607d6e;
    }
  }
}
#email-source {
  padding: 10px;
  padding-top: 5px;
  padding-bottom: 20px;
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

.error-message {
  color: crimson;
  font-size: 1.1em;
}
.analysis {
  margin-top: 20px;
}
</style>
