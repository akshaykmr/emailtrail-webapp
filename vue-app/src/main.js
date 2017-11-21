// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import AnalyseEmail from './components/AnalyseEmail';
import AnalyseHeader from './components/AnalyseHeader';

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#analyse-email',
  template: '<AnalyseEmail />',
  components: { AnalyseEmail },
});

new Vue({
  el: '#analyse-header',
  template: '<AnalyseHeader />',
  components: { AnalyseHeader },
});
