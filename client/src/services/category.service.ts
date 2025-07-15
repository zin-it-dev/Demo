import axios from "@/libs/configs/axios";
import type { ListCategory } from "@/types/category.type";

export const getCategories = async () => {
    const response = await axios.get<ListCategory>("/categories/");
    return response.data.result;
};
