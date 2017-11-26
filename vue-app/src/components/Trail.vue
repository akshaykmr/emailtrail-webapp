<template>
  <div class="trail">
    <div class="utcOffsetSelector">
      <!-- <v-select v-bind:on-change="onOffsetChange" v-bind:value="selectedOffset" placeholder="UTC offset" :options="utcOffsets"></v-select> -->
    </div>
    <Header v-bind:utcOffset="selectedOffset" v-for="(hop, index) in trail" v-bind:key="index" v-bind:headerDetails="hop"></Header>
  </div>
</template>

<script>
import vSelect from "vue-select"
import utcOffsets from './utcOffsets';
import Header from './Header';

export default {
  name: 'Trail',
  props: ['trail'],
  computed: {
  },
  methods: {
    onOffsetChange(val) {
      this.selectedOffset = val;
    },
  },
  data() {
    return {
      selectedOffset: "🌍 Local",
      utcOffsets
    }
  },
  components: {
    Header,
    vSelect
  }
};
</script>

<style lang="scss">
.trail {
  position: relative;
  width: 100%;
  background-color: white;

  &::after {
    content: '';
    display: block;
    position: absolute;
    top: 0;
    left: calc(50% - 5px);
    z-index: 1;
    width: 5px;
    height: 100%;
    border-radius: 10px;
    background-color: darksalmon;
  }
  .utcOffsetSelector {
    float: right;
    margin-right: 70px;
    width: 110px;
    font-family: inherit !important;

    .dropdown-menu {
      width: 110px !important;
    }
  }
}
</style>
