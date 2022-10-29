import java.io.*;
import java.util.*;
import java.lang.Math;
class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(br.readLine());
        for(int test_case = 1; test_case <= T; test_case++)
		{
			float N=Integer.parseInt(br.readLine());
			int ans=0;
            for(int ccase=1;ccase<=N;ccase++)
            {
                StringTokenizer st=new StringTokenizer(br.readLine()," ");
             	double x=Double.parseDouble(st.nextToken());
                double y=Double.parseDouble(st.nextToken());
                double cir=Math.pow((Math.pow(x,2)+Math.pow(y,2)),0.5);
                int tmp = 10-(int)(cir/20);
                if (cir%20==0){
                    tmp+=1;
                }
                if(cir>200){
                    tmp=0;
                }
                if(x==0&&y==0){
                    tmp=10;
                }
                ans+=tmp;
                
            }
            System.out.printf("#%d %d\n",test_case,ans);
        }
	}
}