window.addEventListener('load', function() {
    function fetchAndFill(selectElement) {
        if (!selectElement) return;
        const row = selectElement.closest('.inline-related');
        if (!row) return;

        const lang = selectElement.value;
        const targetMainTopicInput = row.querySelector('input[id$="-mainTopic"]');
        const targetSlugInput = row.querySelector('input[id$="-slug"]');
        const parentMainTopicInput = document.getElementById('id_mainTopic');
        const parentMainTopic = parentMainTopicInput ? parentMainTopicInput.value : '';

        if (!lang) {
            if (targetMainTopicInput && !targetMainTopicInput.value) targetMainTopicInput.value = '';
            return;
        }

        if (parentMainTopic && targetMainTopicInput && !targetMainTopicInput.value) {
            targetMainTopicInput.placeholder = "Loading translation...";
            fetch(`/api/v1/chanting/admin/topic-translations/?topic=${encodeURIComponent(parentMainTopic)}&lang=${encodeURIComponent(lang)}`)
                .then(response => {
                    if (response.ok) return response.json();
                    targetMainTopicInput.placeholder = "Failed to load";
                    return null;
                })
                .then(data => {
                    if (data && data.translated_topic) {
                        targetMainTopicInput.value = data.translated_topic;
                    } else if (data) {
                        targetMainTopicInput.placeholder = "No translation found";
                    }
                })
                .catch(err => {
                    console.error("Error fetching translated topic:", err);
                    targetMainTopicInput.placeholder = "Error fetching";
                });
        }

        // Add suffix logic to slug
        if (targetSlugInput && !targetSlugInput.value) {
            const parentSlugInput = document.getElementById('id_slug');
            if (parentSlugInput && parentSlugInput.value) {
                targetSlugInput.value = parentSlugInput.value + '-' + lang;
            }
        }
    }

    // 1. Handle manual changes
    document.body.addEventListener('change', function(event) {
        const select = event.target;
        if (select.tagName === 'SELECT' && select.id.includes('translations-') && select.id.endsWith('-language')) {
            // Force clear the current main topic so it fetches the new one
            const row = select.closest('.inline-related');
            if (row) {
                const targetMainTopicInput = row.querySelector('input[id$="-mainTopic"]');
                const targetSlugInput = row.querySelector('input[id$="-slug"]');
                if (targetMainTopicInput) targetMainTopicInput.value = '';
                if (targetSlugInput) targetSlugInput.value = '';
            }
            fetchAndFill(select);
        }
    });

    // 2. Handle initial page load (for the default 'extra' forms)
    const existingSelects = document.querySelectorAll('select[id^="id_translations-"][id$="-language"]');
    existingSelects.forEach(select => {
        // Only autofill if it's an empty inline (no id value)
        const row = select.closest('.inline-related');
        if (row && row.classList.contains('has_original')) return; // skip already saved ones
        fetchAndFill(select);
    });

    // 3. Handle when admin user clicks "+ Add another"
    if (typeof django !== 'undefined' && django.jQuery) {
        django.jQuery(document).on('formset:added', function(event, $row, formsetName) {
            if (formsetName === 'translations') {
                const select = $row[0].querySelector('select[id$="-language"]');
                fetchAndFill(select);
            }
        });
    }
});
