import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the cookies function below.
     */
    static void minHeap(int[] A){
        int n= A.length;
        for(int i=n/2;i>=0;i--){
            minHeapify(A,i);
        }
    }
    static void minHeapify(int[] A,int i){
        int l=i*2;
        int r=i*2+1;
        int min;
        if(l<A.length && A[l]<A[i]){
            min=l;
        }else{
            min=i;
        }
        if(r<A.length && A[r]<A[min]){
            min=r;
        }
        if(min!=i){
            int temp=A[i];
            A[i]=A[min];
            A[min]=temp;
            minHeapify(A,min);
        }
    }
    static int cookies(int k, int[] A) {
        minHeap(A);
        int primero=0;
        while(A[primero]<k){
            if(A.length<2)
                return -1;
            A[primero+1]=A[primero]+2*A[primero+1];
            A[primero]=0;
            primero++;
            minHeapify(A,primero);
        }
        return primero;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0].trim());

        int k = Integer.parseInt(nk[1].trim());

        int[] A = new int[n];

        String[] AItems = scanner.nextLine().split(" ");

        for (int AItr = 0; AItr < n; AItr++) {
            int AItem = Integer.parseInt(AItems[AItr].trim());
            A[AItr] = AItem;
        }

        int result = cookies(k, A);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}
