```java
/*
최대 매출(Sliding Window)
현수의 아빠는 제과점을 운영합니다. 현수아빠는 현수에게 N일 동안의 매출기록을 주고 연속
된 K일 동안의 최대 매출액이 얼마인지 구하라고 했습니다.
만약 N=10이고 10일 간의 매출기록이 아래와 같습니다. 이때 K=3이면
12 15 11 20 25 10 20 19 13 15
연속된 3일간의 최대 매출액은 11+20+25=56만원입니다.
여러분이 현수를 도와주세요.
▣ 입력설명
첫 줄에 N(5<=N<=100,000)과 K(2<=K<=N)가 주어집니다.
두 번째 줄에 N개의 숫자열이 주어집니다. 각 숫자는 500이하의 음이 아닌 정수입니다.
▣ 출력설명
첫 줄에 최대 매출액을 출력합니다.
▣ 입력예제 1
10 3
12 15 11 20 25 10 20 19 13 15
▣ 출력예제 1
56
*/

// 내가 작성한 답안
package PS;

import java.util.*;
public class Inflearn03_03{
	/*
	3일치 매출을 계산할 때는, 매차례 일일이 세 번 더하지 않는다.
	대신 <이전 차례 기준> 3일치 총매출에서 <1일차 매출>을 빼고, <4일차 매출>을 더하면,
	지금 차례의 3일치 매출을 구할 수 있다.
	지금 차례에서 계산한 3일치 매출 vs. 현재 max값을 비교해서 계속 갱신해나가고
	최후에 얻어낸 max값이 최대 매출액이 될 것이다.
	*/
	
	public int solution(int totalDays, int range, int[] profits) {
//		우선 profitBefore값을 첫 3일의 매출액으로 초기화
		int profitBefore = 0;
		for(int i=0; i<range; i++) {
			profitBefore += profits[i];
		}		
//		maxProfit 초기화
		int maxProfit = profitBefore;
//		1일차 매출과 4일차 매출을 가리킬 두 포인터를 초기화
		int firstPointer = 0;
		int lastPointer = range;
		
		while(lastPointer < totalDays) {
			int currentProfit = profitBefore - profits[firstPointer] + profits[lastPointer];

			if (currentProfit > maxProfit) {
				maxProfit = currentProfit;
			}
//			갱신
			profitBefore = currentProfit;
			firstPointer++;
			lastPointer++;
		}
		
		return maxProfit;
	}
	
	public static void main(String[] args){
		Inflearn03_03 T = new Inflearn03_03();
		Scanner sc = new Scanner(System.in);
		
		String[] days = sc.nextLine().split(" ");

		int totalDays = Integer.parseInt(days[0]);
		int range = Integer.parseInt(days[1]);
		int[] profits = new int[totalDays];
		
		for(int i=0; i<totalDays; i++) {
			profits[i] = sc.nextInt();
		}
		
		int maxProfit = T.solution(totalDays, range, profits);
		System.out.println(maxProfit);
	}
}

// 강의 해설
package PS;

import java.util.*;
public class Inflearn03_03{
	/*
	로직은 똑같으나 이 코드가 for문과 Math.max()를 써서 훨~~~씬 짧음.
	*/
	public int solution(int totalDays, int range, int[] profits) {
		// 우선 sumOfRange값을 첫 3일의 매출액으로 초기화
		int sumOfRange = 0;
		for(int i=0; i<range; i++) sumOfRange += profits[i];
		
		int maxProfit = sumOfRange; // maxProfit 초기화
		for(int i=range; i<totalDays; i++) {
			sumOfRange = sumOfRange + (profits[i] - profits[i-range]);
			maxProfit = Math.max(maxProfit, sumOfRange);
		}
		return maxProfit;
	}
	
	public static void main(String[] args){
		Inflearn03_03 T = new Inflearn03_03();
		Scanner sc = new Scanner(System.in);
		
		int totalDays = sc.nextInt();
		int range = sc.nextInt();
		int[] profits = new int[totalDays];
		for(int i=0; i<totalDays; i++) profits[i] = sc.nextInt();
		
		int maxProfit = T.solution(totalDays, range, profits);
		System.out.println(maxProfit);
	}
}
```

### 복잡도
O(n)
### 배운점
- 이 접근법을 **Sliding Window**라고 부른다는 것(주어진 배열을, 주어진 범위(k)만큼 토막토막 탐색하는 방법이 마치 고정된 크기의 창문을 옆으로 미는 것과 같아서 Sliding Window라고 불린다고...)
- Sliding window 문제는 굳이 포인터를 두 개 두지 않아도 풀 수 있다. (`sumOfRange`값에서 빼고 싶은 앞쪽의 원소는 `profits[i - range]`로 간단히 찾을 수 있기 때문)
- 자바의 `Math.max()` 메소드를 쓰자.
