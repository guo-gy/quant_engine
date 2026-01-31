const { exec } = require('child_process');

async function getPrice(token) {
    return new Promise((resolve) => {
        // 使用 CoinGecko 公开 API (不需要 key，但有频率限制)
        const url = `https://api.geckoterminal.com/api/v2/networks/solana/pools/` + token; 
        // 这里简化逻辑，直接抓取几个主要池子
        exec('curl -s "' + url + '"', (error, stdout) => {
            if (error) resolve(null);
            try {
                const data = JSON.parse(stdout);
                resolve(data.data?.attributes?.base_token_price_usd || null);
            } catch (e) {
                resolve(null);
            }
        });
    });
}

async function run() {
    // 使用 GeckoTerminal 的 Pool ID
    const pools = {
        'SOL/USDC': '58oQChx4yWmvKpgbbZfYSGawU4D6p3U2T5t6E69Wf4v6', // Raydium
        'JUP/SOL': '2TH9uX7zQz8SfsGvD6YfsX8W6y5C1Y3W4X5W6X7W8X9Z' // 这里其实可以用更简单的办法
    };

    // 换个更直接的办法：使用 binance 接口获取 SOL 价格
    exec('curl -s "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"', (err, stdout) => {
        let solPrice = "N/A";
        try {
            solPrice = JSON.parse(stdout).price;
        } catch(e) {}
        
        console.log("SOL Price: $" + solPrice);
    });
}
run();
