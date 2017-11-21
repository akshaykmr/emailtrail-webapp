<template>
  <div id="analyse-header">
    <p>
      You can also analyse a single <code>Received</code> header <a href="" class="load-sample" v-on:click="loadsampleHeader($event)"><b> Load sample "Recieved" header 👇</b></a>
    </p>
    <div id ="header-form">
      <textarea class="glowing-border" id="header-source" rows="9" v-model="header"
      placeholder="Paste a header and then click analyse 🔍">
      </textarea>
      <div class="submit-button" v-bind:class="{ disabled: header.trim() === ''}" v-on:click="analyseHeader">
        {{submitButtonMessage}}
      </div>
    </div>
    <div class="loader" v-if="loading">
    </div>
    <div class="error-message" v-if="error">
      {{errorMessage}}
    </div>

    <div class="analysis" v-if="analysisExists">
      <div v-if="!loading">
        lorem
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';
import sampleHeader from './sampleHeader';

export default {
  name: 'AnalyseHeader',
  data() {
    return {
      header: '',
      analysis: {},
      loading: false,
      error: false,
      lastAnalysedHeader: '',
      errorMessage: 'Something went wrong... Check your input or try again, else reach me on twitter: @uberakshay',
    };
  },
  computed: {
    analysisExists: function() {
      return this.lastAnalysedHeader === this.header.trim() && this.header.trim() !== '';
    },

    submitButtonMessage: function() {
      if(this.analysisExists) {
        return 'Analysis 👇';
      } else if (this.loading) {
        return 'Analysing 🔎'
      }
      return 'Analyse ☝️';
    },
  },
  methods: {
    loadsampleHeader: function(event) {
      if (event) event.preventDefault()
      this.header = sampleHeader
    },

    analyseHeader: function () {
      const header = this.header.trim();
      if(!header || this.loading) return;

      this.loading = true;
      axios.post('/api/v1/analyse', header)
        .then((response) => {
          this.analysis = response.data.analysis
          this.error = '';
          this.loading = false;
          this.lastAnalysedHeader = header;
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
#header-form {
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
    width: 160px;
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
#header-source {
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
  max-width: 500px;
  margin: 0 auto;
  margin-top: 20px;
}

a.load-sample {
  color: #5ab9cf;
}
</style>
