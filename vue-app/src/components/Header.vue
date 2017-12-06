<template>
  <div class="header" v-bind:class="{ hasDelay }">
    <span v-if="hasDelay" class="delay">
      {{duration}}
    </span>
    <div v-if="headerDetails.timestamp !== ''" class="calender-time">
      <span>{{ calenderTime }}</span>
    </div>
    <div v-if="headerDetails.protocol !== ''" class="protocol">
      <span> {{headerDetails.protocol}} </span>
    </div>
    <div class="from-by-fields">
      <div v-if="headerDetails.from !== ''" class="from">
        <span> <span class="field">From:</span> <span class="value"> {{headerDetails.from}} </span></span>
      </div>
      <div v-if="headerDetails.receivedBy !== ''" class="by">
        <span> <span class="field">By:</span> <span class="value"> {{headerDetails.receivedBy}}</span> </span>
      </div>
    </div>
  </div>
</template>

<script>

import moment from 'moment';

export default {
  name: 'Header',

  computed: {
    calenderTime: function() {
      let time = moment.unix(this.headerDetails.timestamp);
      if(this.utcOffset !== '🌍 Local') {
        debugger // BUG Why doesn't this work
        time = time.zone(this.utcOffset);
      }
      const str = time.format("dddd, MMMM Do YYYY, h:mm:ss a");
      return str
    },
    hasDelay: function() {
      const { delay } = this.headerDetails;
      return typeof(delay) === 'number' && delay > 0;
    },
    duration: function(){
      const { delay } = this.headerDetails;
      if(delay < 60) {
        return `${delay} second${delay > 1 ? 's':''}`
      }
      return moment.duration(this.headerDetails.delay, 'seconds').humanize();
    }
  },

  methods: {

  },
  props: ['headerDetails', 'utcOffset']
};
</script>

<style lang="scss">
$calender-color: #0e4246;
.header {
  position: relative;
  background-color:  honeydew;
  border: 1px solid $calender-color;
  max-width: calc(100% - 20px);
  margin: 10px;
  margin-bottom: 25px;
  padding-bottom: 10px;
  z-index: 2;
  border-radius: 10px;
  box-shadow: 0px 0px 13px -7px rgba(0,0,0,0.75);

  &.hasDelay {
    margin-top: 100px;
  }
  .from-by-fields {
    margin-top: 8px;
    .field {
      color: #0f383b;
    }

    .from, .by {
      padding: 5px;
      text-align: center;
    }

    .from {
      .value {
        color: #0f383b;
      }
    }

    .by {
      font-size: 1.35em;
      font-weight: bolder;
      .value {
        color: #0f383b;
      }
    }
  }

  .calender-time {
    color: white;
    text-align: center;
    font-size: 1.1em;

    span {
      display: inline-block;
      background-color: $calender-color;
      padding: 7px;
      border-bottom-left-radius: 5px;
      border-bottom-right-radius: 5px;
    }
  }

  .protocol {
    text-align: center;
    text-transform: uppercase;
    margin-top: 10px;
    span {
      color: white;
      background-color: burlywood;
      padding: 5px;
      border-radius: 5px;
    }
  }

  .delay {
    position: absolute;
    display: inline-block;
    width: 240px;
    height: 50px;
    border-radius: 10px;
    left: calc(50% - 120px);
    top: calc(-75px);
    color: white;
    background-color: darksalmon;
    line-height: 50px;
    text-align: center;
    font-size: 1.1em;
    box-shadow: 0px 0px 13px -7px rgba(0,0,0,0.75);

    &::after {
      position: absolute;
      content: '';
      display: block;
      height: 50px;
      width: 50px;
      top: 0;
      left: -60px;
      background-image: url('/static/images/clock.svg');
      background-repeat: no-repeat;
      background-position: center;
    }
  }

}
</style>
