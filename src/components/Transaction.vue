<template>
  <li>
      <span></span>
  </li>
</template>

<script>
export default {
  props: [
    'transaction'
  ]
}
</script>

<style lang="scss" scoped>
li {
  background-color: #fff;
  box-shadow: $box-shadow;
  color: #333;
  display: flex;
  justify-content: space-between;
  position: relative;
  padding: 10px;
  margin: 10px 0;

    &.plus {
        border-right: 5px solid #2ecc71;
    }

    &.minus {
        border-right: 5px solid #c0392b;
    }

}
</style>