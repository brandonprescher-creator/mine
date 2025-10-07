/**
 * Parent Dashboard JavaScript
 * Interactive features for mission control
 */

// Schedule a lesson for a student
function openScheduler(studentId) {
    const date = prompt("Enter date (YYYY-MM-DD):");
    if (!date) return;

    // TODO: Open a modal with lesson selector
    // For now, use a simple prompt
    const lessonId = prompt("Enter lesson ID:");
    if (!lessonId) return;

    fetch('/parent/schedule-lesson', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            student_id: studentId,
            lesson_id: parseInt(lessonId),
            date: date
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'scheduled') {
            alert(`Lesson scheduled for ${date}!`);
            location.reload();
        }
    })
    .catch(error => console.error('Error:', error));
}

// Create a learning playlist
function openPlaylistCreator(studentId) {
    const name = prompt("Enter playlist name:");
    if (!name) return;

    const lessonIds = prompt("Enter lesson IDs (comma-separated):");
    if (!lessonIds) return;

    const ids = lessonIds.split(',').map(id => parseInt(id.trim()));

    fetch('/parent/create-playlist', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            student_id: studentId,
            name: name,
            lesson_ids: ids
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.playlist_id) {
            alert(`Playlist "${name}" created with ${data.lesson_count} lessons!`);
        }
    })
    .catch(error => console.error('Error:', error));
}

// Update student interests
function openInterests(studentId) {
    const interests = prompt("Enter interests (comma-separated):");
    if (!interests) return;

    const interestList = interests.split(',').map(i => i.trim());

    fetch('/parent/update-interests', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            student_id: studentId,
            interests: interestList
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Interests updated! New lesson suggestions available.');
            location.reload();
        }
    })
    .catch(error => console.error('Error:', error));
}

// Create a reward
function createReward() {
    const studentId = prompt("Student ID (student_1 or student_2):");
    if (!studentId) return;

    const rewardName = prompt("Reward name (e.g., 'Movie Night'):");
    if (!rewardName) return;

    const requirementType = prompt("Requirement type (lessons_completed or mastery_level):");
    if (!requirementType) return;

    const requirementValue = parseInt(prompt("How many to earn the reward?:"));
    if (!requirementValue) return;

    fetch('/parent/create-reward', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            student_id: studentId,
            reward_name: rewardName,
            requirement: {
                type: requirementType,
                value: requirementValue
            }
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.coupon_id) {
            alert(`Reward "${rewardName}" created!`);
        }
    })
    .catch(error => console.error('Error:', error));
}

// Print certificates
function printCertificates() {
    window.location.href = '/parent/certificates';
}

// Auto-refresh every 5 minutes to get latest data
setInterval(() => {
    location.reload();
}, 5 * 60 * 1000);

