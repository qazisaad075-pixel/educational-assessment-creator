async function generateAssessment() {

    const subject = document.getElementById("subject").value;
    const grade_level = document.getElementById("grade_level").value;
    const topic = document.getElementById("topic").value;

    const output = document.getElementById("output");

    output.innerHTML = "⏳ Generating assessment...";

    try {
        const response = await fetch("https://educational-assessment-creator.onrender.com/create-assessment", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                subject: subject,
                grade_level: parseInt(grade_level),
                topic: topic
            })
        });

        const data = await response.json();

        output.innerHTML = `
            <h2>📊 Assessment Generated</h2>
            <pre>${JSON.stringify(data, null, 2)}</pre>
        `;

    } catch (error) {
        output.innerHTML = "❌ Error generating assessment";
        console.log(error);
    }
}