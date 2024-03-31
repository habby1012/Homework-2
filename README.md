# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

>這題原輸出只有第一行，為了顯示各個swap的過程，我多print出了下面四行。
<img width="603" alt="image" src="https://github.com/habby1012/Homework-2/assets/80194639/892ded36-29d9-43eb-b71d-1851bd8274a3">



## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> 當某個token y被交易者不斷買入時，y會相對於x變少很多，導致價格迅速上漲，這就是slippage。
> 以下舉[Uniswap](https://github.com/Uniswap/v2-periphery/blob/master/contracts/UniswapV2Router02.sol)裡面的function當作例子。
> 
> <img width="625" alt="image" src="https://github.com/habby1012/Homework-2/assets/80194639/38351436-6c07-471e-8dc0-a62b38aeb51e">
>
> 可以看到require那一行，根據計算出的輸出數量，檢查最終輸出數量是否滿足用戶設定的amountOutMin。如果不滿足，交易就會失敗，這保護了交易者不會因slippage太大而損失過多。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> 1. 如果沒有扣除minimum liquidity，那第一個提供者可以投入一個很小的資產，就能得到現在池子裡的幣，也就意味著只要他們稍微增加資產，就可以不成比例得提高幣的價格。
> 2. 可以確保只少有一個最小的流動性被鎖定住，避免一開始池子就過於薄弱，導致價格在最早期就受到很大的波動。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> 1. 可以確保新加入的提供者獲得的幣數量跟他們貢獻成正比。代表無論你是什麼時候加入，你得到的份額就是你對池中的實際貢獻。
> 2. 當某人添加幣的時候，實際上是按照當前的市場價格進行操作的，確保公正。

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> 當我要準備進行一個大交易時，攻擊者會監控到，並且提早先做一個同樣資產的交易，讓價格推高，接著我會變成以更高的價格去購買資產。最後，攻擊者在我交易完後馬上執行賣出的交易，因為剛剛我交易的影響，所以現在資產價格仍然在高點，所以攻擊者就能用高於市場價的價格賣出，賺取差價。
> 這樣的後果就是，我會以更高的市場價格去購買幣，增加了我的交易成本，如果我剛好又把slippage範圍設的很寬鬆，那我可能就會以對我很不利的價格成交。
