export type Category = {
    id: number;
    name: string;
};

export type ListCategory = {
    result: Pick<Category, "id" | "name">[];
};
