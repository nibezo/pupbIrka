<template>
  <div>
    <HeaderComponent />
    <main>{{ message }}</main>
  </div>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue'
import { ref, onMounted } from 'vue';

export default {
  components: {
    HeaderComponent
  },
  setup() {
    const message = ref('');

    onMounted(() => {
      fetch('http://localhost:8000/')
        .then((response) => response.json())
        .then((data) => {
          message.value = data.message;
        });
    });

    return { message };
  },
};
</script>

