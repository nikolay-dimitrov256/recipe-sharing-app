document.addEventListener('DOMContentLoaded', function () {
    const ingredientsContainer = document.getElementById('ingredients-container');
    const addIngredientBtn = document.getElementById('add-ingredient');
    const ingredientsJsonInput = document.getElementById('ingredients-json');

    // Add new ingredient row
    addIngredientBtn.addEventListener('click', function () {
        const newRow = document.createElement('div');
        newRow.classList.add('ingredient-row');

        // Create ingredient name input
        const nameInput = document.createElement('input');
        nameInput.type = 'text';
        nameInput.name = 'ingredient_name';
        nameInput.placeholder = 'Product name';

        // Create ingredient quantity input
        const quantityInput = document.createElement('input');
        quantityInput.type = 'text';
        quantityInput.name = 'ingredient_quantity';
        quantityInput.placeholder = 'Quantity';

        // Create remove button
        const removeButton = document.createElement('button');
        removeButton.type = 'button';
        removeButton.classList.add('remove-ingredient');
        removeButton.classList.add('reject');
        removeButton.textContent = 'Remove';

        // Append elements to the row
        newRow.appendChild(nameInput);
        newRow.appendChild(quantityInput);
        newRow.appendChild(removeButton);
        ingredientsContainer.appendChild(newRow);
    });

    // Remove ingredient row
    ingredientsContainer.addEventListener('click', function (event) {
        if (event.target.classList.contains('remove-ingredient')) {
            event.target.closest('.ingredient-row').remove();
        }
    });

    // Serialize ingredients to JSON on form submission
    document.getElementById('products-form').addEventListener('submit', function () {
        const ingredients = {};
        document.querySelectorAll('.ingredient-row').forEach(row => {
            const name = row.querySelector('[name="ingredient_name"]').value.trim();
            const quantity = row.querySelector('[name="ingredient_quantity"]').value.trim();
            if (name) {
                ingredients[name] = quantity;
            }
        });
        ingredientsJsonInput.value = JSON.stringify(ingredients);
    });
});