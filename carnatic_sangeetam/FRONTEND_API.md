# Carnatic Questions Frontend API Integration

Base prefix: `/api/v1/`

Module endpoints:

- `GET, POST /api/v1/carnatic-categories/`
- `GET, PUT, PATCH, DELETE /api/v1/carnatic-categories/:id/`
- `GET, POST /api/v1/carnatic-questions/`
- `GET, PUT, PATCH, DELETE /api/v1/carnatic-questions/:id/`
- `GET, POST /api/v1/carnatic-syllabus/`
- `GET, PUT, PATCH, DELETE /api/v1/carnatic-syllabus/:id/`
- `GET /api/v1/carnatic-syllabus/categories/`
- `GET, POST /api/v1/carnatic-kacheri/`
- `GET, PUT, PATCH, DELETE /api/v1/carnatic-kacheri/:id/`
- `GET, POST /api/v1/carnatic-lesson-practice/`
- `GET, PUT, PATCH, DELETE /api/v1/carnatic-lesson-practice/:id/`

All module endpoints are public and currently use `AllowAny`.

## Category CRUD API

Use this API for category listing, create, edit, and delete.

### List response

```json
[
  {
    "id": 9,
      "order": 1,
    "name": "10) Composition Forms",
      "colorCode": "#0EA5E9",
    "created_at": "2026-04-24T10:00:00Z",
    "updated_at": "2026-04-24T10:00:00Z"
  },
  {
    "id": 12,
      "order": 2,
    "name": "Sarali Varisaigal",
      "colorCode": "#22C55E",
    "created_at": "2026-04-24T10:00:00Z",
    "updated_at": "2026-04-24T10:00:00Z"
  }
]
```

### Create request

```json
{
  "order": 3,
  "colorCode": "#F59E0B",
  "name": "Geethams"
}
```

### Update request

Use `PATCH /api/v1/carnatic-categories/:id/`

```json
{
  "order": 4,
  "colorCode": "#EF4444",
  "name": "Advanced Geethams"
}
```

### Delete request

Use `DELETE /api/v1/carnatic-categories/:id/`

### Filters

Example:

`GET /api/v1/carnatic-categories/?query=geetham`

Supported query params:

- `query=<text>` searches category name
- Category list is returned ordered by `order` and then `name`

## Category helper

Use this to populate syllabus and question category dropdowns.

Endpoint:

`GET /api/v1/carnatic-syllabus/categories/`

Response:

```json
{
  "categories": [
    "10) Composition Forms",
    "Sarali Varisaigal"
  ],
  "category_options": [
    {
      "id": 9,
      "name": "10) Composition Forms",
      "order": 1,
      "colorCode": "#0EA5E9",
      "created_at": "2026-04-24T10:00:00Z",
      "updated_at": "2026-04-24T10:00:00Z"
    },
    {
      "id": 12,
      "name": "Sarali Varisaigal",
      "order": 2,
      "colorCode": "#22C55E",
      "created_at": "2026-04-24T10:00:00Z",
      "updated_at": "2026-04-24T10:00:00Z"
    }
  ]
}
```

Frontend guidance:

- Show `name` in the dropdown.
- Submit `id` as the `category` field in create and update requests.
- Use `colorCode` to render category chips/badges in frontend.
- Use the dedicated category CRUD API for category management screens.

## Carnatic Questions API

### Response shape

```json
{
  "id": 15,
  "category": 12,
  "category_name": "Sarali Varisaigal",
  "question": "What is Sarali Varisai?",
  "answer": "It is the basic exercise...",
  "audio": "https://admin.askharekrishna.com/media/carnatic_questions/audio/file.mp3",
  "created_at": "2026-04-24T10:00:00Z",
  "updated_at": "2026-04-24T10:00:00Z"
}
```

### Create request

JSON request:

```json
{
  "category": 12,
  "question": "What is Sarali Varisai?",
  "answer": "It is the basic exercise..."
}
```

If uploading audio, use `multipart/form-data`:

- `category`
- `question`
- `answer`
- `audio`

### Filters

`GET /api/v1/carnatic-questions/?category=12&query=sarali`

Supported query params:

- `category=<id or category name>`
- `division=<category name>` as backward-compatible alias
- `query=<text>` searches question, answer, and category name

## Carnatic Syllabus API

Syllabus list is paginated.

### Paginated list response

```json
{
  "count": 182,
  "next": "https://admin.askharekrishna.com/api/v1/carnatic-syllabus/?page=2",
  "previous": null,
  "results": [
    {
      "id": 160,
      "category": 9,
      "category_name": "10) Composition Forms",
      "topic": "Anupallavi Section",
      "lesson": "Long lesson content...",
      "audioPath": null,
      "videoPath": "https://www.youtube.com/watch?v=abc123",
      "videoSamples": [
        {
          "id": 1,
          "url": "https://www.youtube.com/watch?v=abc123",
          "sort_order": 0
        },
        {
          "id": 2,
          "url": "https://www.youtube.com/watch?v=def456",
          "sort_order": 1
        }
      ],
      "created_at": "2026-03-25T03:57:36.620634Z",
      "updated_at": "2026-03-25T03:57:36.620641Z"
    }
  ]
}
```

Notes:

- `videoSamples` is the real multi-video field.
- `videoPath` is a compatibility field and returns the first video sample URL.
- New frontend code should use `videoSamples`.

### Create request without file upload

Use JSON:

```json
{
  "category": 12,
  "topic": "Sarali Varisai 1",
  "lesson": "Lesson text here",
  "videoSamples": [
    {
      "url": "https://www.youtube.com/watch?v=abc123",
      "sort_order": 0
    },
    {
      "url": "https://www.youtube.com/watch?v=def456",
      "sort_order": 1
    }
  ]
}
```

You can omit `sort_order`. If omitted, backend uses array order.

### Create or update request with audio upload

Use `multipart/form-data`:

- `category`
- `topic`
- `lesson`
- `audioPath`
- `videoSamples` as a JSON string

Example `videoSamples` form value:

```json
[
  {
    "url": "https://www.youtube.com/watch?v=abc123",
    "sort_order": 0
  },
  {
    "url": "https://www.youtube.com/watch?v=def456",
    "sort_order": 1
  }
]
```

Example frontend `FormData`:

```js
const formData = new FormData();
formData.append('category', String(categoryId));
formData.append('topic', topic);
formData.append('lesson', lesson);
formData.append('audioPath', audioFile);
formData.append('videoSamples', JSON.stringify([
  { url: 'https://www.youtube.com/watch?v=abc123', sort_order: 0 },
  { url: 'https://www.youtube.com/watch?v=def456', sort_order: 1 }
]));
```

### Update behavior

Use `PATCH /api/v1/carnatic-syllabus/:id/`

Important:

- When `videoSamples` is sent, backend replaces the entire video list for that syllabus.
- For reordering, send the full reordered array, not only the changed item.

Reorder example:

```json
{
  "videoSamples": [
    {
      "url": "https://www.youtube.com/watch?v=def456",
      "sort_order": 0
    },
    {
      "url": "https://www.youtube.com/watch?v=abc123",
      "sort_order": 1
    }
  ]
}
```

### Filters

Example:

`GET /api/v1/carnatic-syllabus/?category=9&query=practice&page=1&page_size=20`

Supported query params:

- `category=<id or category name>`
- `division=<category name>` as backward-compatible alias
- `query=<text>` searches topic, lesson, and category name
- `page=<number>`
- `page_size=<number>`

## Carnatic Kacheri API

This endpoint is for kacheri video entries.

### Response shape

```json
{
  "id": 1,
  "title": "Kalyani RTP at Music Academy",
  "singer": "M. S. Subbulakshmi",
  "ragam": "Kalyani",
  "videoUrl": "https://www.youtube.com/watch?v=xyz123",
  "description": "Concert excerpt and notes.",
  "created_at": "2026-04-24T12:00:00Z",
  "updated_at": "2026-04-24T12:00:00Z"
}
```

### Paginated list response

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Kalyani RTP at Music Academy",
      "singer": "M. S. Subbulakshmi",
      "ragam": "Kalyani",
      "videoUrl": "https://www.youtube.com/watch?v=xyz123",
      "description": "Concert excerpt and notes.",
      "created_at": "2026-04-24T12:00:00Z",
      "updated_at": "2026-04-24T12:00:00Z"
    }
  ]
}
```

### Create request

```json
{
  "title": "Kalyani RTP at Music Academy",
  "singer": "M. S. Subbulakshmi",
  "ragam": "Kalyani",
  "videoUrl": "https://www.youtube.com/watch?v=xyz123",
  "description": "Concert excerpt and notes."
}
```

### Update request

Use `PATCH /api/v1/carnatic-kacheri/:id/`

Example:

```json
{
  "title": "Updated concert title",
  "ragam": "Bhairavi",
  "description": "Updated concert note"
}
```

### Filters

Example:

`GET /api/v1/carnatic-kacheri/?singer=subbulakshmi&ragam=kalyani&query=concert`

Supported query params:

- `title=<text>`
- `singer=<text>`
- `ragam=<text>`
- `query=<text>` searches title, singer, ragam, and description

## Carnatic Lesson Practice API

Use this API for lesson practice tracks (e.g. Sarali Varisaigal, Jantai Varisaigal, etc.).

### Response shape (List / Detail)

`GET /api/v1/carnatic-lesson-practice/`
`GET /api/v1/carnatic-lesson-practice/:id/`

```json
[
  {
    "id": 1,
    "PracticeCategory": "Swaravali/Sarali Varisaigal",
    "lessonName": "Sarali Varisai 1",
    "swarams": "S R G M | P D | N S ||\nS N D P | M G | R S ||",
    "audioPath": "https://admin.askharekrishna.com/media/carnatic_lesson_practice/sarali_varisai_1.mp3",
    "audios": [
      {
        "id": 1,
        "audioPathName": "1st Speed (Prathama Kaalam)",
        "audioPath": "https://admin.askharekrishna.com/media/carnatic_lesson_practice/audio/sarali_1_speed1.mp3",
        "sort_order": 0,
        "created_at": "2026-08-25T15:22:17.842105Z",
        "updated_at": "2026-08-25T15:22:17.842117Z"
      },
      {
        "id": 2,
        "audioPathName": "2nd Speed (Dvithiya Kaalam)",
        "audioPath": "https://admin.askharekrishna.com/media/carnatic_lesson_practice/audio/sarali_1_speed2.mp3",
        "sort_order": 1,
        "created_at": "2026-08-25T15:22:17.842105Z",
        "updated_at": "2026-08-25T15:22:17.842117Z"
      }
    ],
    "videos": [
      {
        "id": 1,
        "youtubevideoUrl": "https://www.youtube.com/watch?v=example123",
        "sort_order": 0,
        "created_at": "2026-08-25T15:22:17.842105Z",
        "updated_at": "2026-08-25T15:22:17.842117Z"
      }
    ],
    "created_at": "2026-05-12T15:55:51.970293Z",
    "updated_at": "2026-05-12T15:55:51.970302Z"
  }
]
```

### Frontend Implementation Guide

#### 1. Home Page / Lesson List: Navigator Card
On the home page under "Listening Focused Practice":
- Display the `PracticeCategory` and `lessonName`.
- Render the card as a navigational link pointing to `/practice/[id]` (or `href={`/practice/${lesson.id}`}`).
- An arrow icon / "Open Practice" indicator can replace the inline audio play button.

#### 2. Dedicated Lesson Detail Page (`/practice/[id]`)
- Display `PracticeCategory` and `lessonName`.
- Render the list of `audios`, each with its `audioPathName` and an interactive audio player.
- If `videos` are present, render embedded YouTube video players (`<iframe src="...">` from the `youtubevideoUrl`).

## Frontend implementation summary

- Use category helper API to build dropdowns.
- Use category CRUD API for category management screens.
- Submit `category` as the category ID.
- Use `videoSamples` as the main syllabus video field.
- Keep `videoPath` only as a read-only compatibility field.
- When reordering syllabus videos, send the full `videoSamples` array.
- Use `carnatic-kacheri` for singer/ragam/video URL based content.
- Use `carnatic-lesson-practice` for lesson cards and detail pages with multiple `audios` and `videos`.
- Use `carnatic-ragam-lessons` for Ragam Lakshana lessons with audios and YouTube video samples.
- Use `carnatic-mridanga-lessons` for Mridanga Tala lessons with Matras, Mantras/Notes, Audios, YouTube Videos, and Kirtan Demo Videos.

## Mridanga Lessons API

Endpoint: `GET, POST /api/v1/carnatic-mridanga-lessons/`
Detail: `GET, PUT, PATCH, DELETE /api/v1/carnatic-mridanga-lessons/:id/`

### Response Shape

```json
{
  "id": 1,
  "tala_name": "Kaharwa Tala",
  "level": "beginner",
  "matras": 8,
  "mantras_and_notes": "Dha Ge Na Tin | Ta Ke Na Dhin",
  "description": "Standard 8-beat cycle widely used in ISKCON kirtan.",
  "sort_order": 0,
  "audios": [
    {
      "id": 1,
      "songName": "Prabhupada Style Kaharwa 1st Speed",
      "audioPath": "https://admin.askharekrishna.com/media/carnatic_mridanga_lessons/audio/kaharwa_speed1.mp3",
      "sort_order": 0,
      "created_at": "2026-08-29T17:15:00Z",
      "updated_at": "2026-08-29T17:15:00Z"
    }
  ],
  "videos": [
    {
      "id": 1,
      "title": "Kaharwa Hand Technique Tutorial",
      "youtubevideoUrl": "https://www.youtube.com/watch?v=tutorial123",
      "sort_order": 0,
      "created_at": "2026-08-29T17:15:00Z",
      "updated_at": "2026-08-29T17:15:00Z"
    }
  ],
  "kirtan_demos": [
    {
      "id": 1,
      "title": "Kaharwa in Live Mangala Arati",
      "youtubevideoUrl": "https://www.youtube.com/watch?v=kirtandemo123",
      "sort_order": 0,
      "created_at": "2026-08-29T17:15:00Z",
      "updated_at": "2026-08-29T17:15:00Z"
    }
  ],
  "created_at": "2026-08-29T17:15:00Z",
  "updated_at": "2026-08-29T17:15:00Z"
}
```

### Filters

- `level=<beginner|medium|advanced>` (e.g., `?level=beginner`)
- `matras=<number>` (e.g., `?matras=8`)
- `query=<text>` (searches Tala name, mantras/notes, and description)