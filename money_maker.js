const { exec } = require('child_process');

async function getPrice(token) {
    return new Promise((resolve) => {
        // 使用 v1 API，通常不需要 API Key
        exec('curl -s "https://price.jup.ag/v1/price?id=' + token + '"', (error, stdout) => {
            if (error) {
                resolve(null);
            }
            try {
                const data = JSON.parse(stdout);
                resolve(data.data?.price || null);
            } catch (e) {
                resolve(null);
            }
        });
    });
}

async function run() {
    const tokens = {
        'SOL': 'So11111111111111111111111111111111111111112',
        'JitoSOL': 'J1tG8ZfAt7mpymsSfsga6oCcS4zZTCU2HJatS3R1S7N',
        'mSOL': 'mSoLzYSa17k7jaREb4WubpS647M9fM6GM7Y3Ymm98i',
        'INF': 'IF9ReArvYWY355L83S79iSjS2kFv2S8YgN1x8f1rX9f',
        'JUP': 'JUPyiS6S6S6S6S6S6S6S6S6S6S6S6S6S6S6S6S6S6S'
    };

    let report = '\n## Market Update - ' + new Date().toISOString() + '\n';
    
    let solPrice = null;
    let infPrice = null;

    for (const [name, id] of Object.entries(tokens)) {
        const price = await getPrice(id);
        if (price) {
            report += '- **' + name + ':** $' + parseFloat(price).toFixed(4) + '\n';
            if (name === 'SOL') solPrice = price;
            if (name === 'INF') infPrice = price;
        } else {
            report += '- **' + name + ':** Failed to fetch\n';
        }
    }

    if (solPrice && infPrice) {
        const ratio = parseFloat(infPrice) / parseFloat(solPrice);
        report += '\n### Analysis\n- **INF/SOL Ratio:** ' + ratio.toFixed(4) + '\n';
        if (ratio < 1.39) {
            report += '- **SIGNAL:** INF is undervalued. Possible yield play.\n';
        } else {
            report += '- **SIGNAL:** INF is fairly priced.\n';
        }
    }

    console.log(report);
}

run();
