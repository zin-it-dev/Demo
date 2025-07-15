<script setup lang="ts">
import { onMounted, ref } from "vue";

import Greeting from "@/components/Greeting.vue";
import type { Category } from "@/types/category.type";
import { getCategories } from "@/services/category.service";

const categories = ref<Category[]>([]);
const loading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
    try {
        categories.value = await getCategories();
    } catch (err) {
        error.value = "Failed to fetch categories.";
        console.error(err);
    } finally {
        loading.value = false;
    }
});
</script>

<template>
    <div>
        <h1>Welcome to Readify !!!</h1>
    </div>
    <Greeting name="ZIN" />

    <div v-if="loading">Loading categories...</div>
    <div v-else-if="error">{{ error }}</div>

    <ul v-else>
        <li v-for="category in categories" :key="category.id">
            {{ category.name }}
        </li>
    </ul>
</template>
