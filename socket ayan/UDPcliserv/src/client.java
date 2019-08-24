import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

 class client {

	public static void main(String args[]) throws IOException {
		int num1,num2,op;
		Scanner sc=new Scanner(System.in);
		DatagramSocket ds=new DatagramSocket();
		System.out.println("say something");
		String msg=sc.next();
		byte[] b=msg.getBytes();
		
		System.out.println("Choose a Option->");
		System.out.println("1.Sum");
		System.out.println("2.Subtract");
		System.out.println("3.Multiply");	
		System.out.println("4.Divide");
		
		op=sc.nextInt();
		
		System.out.println("Enter 2 operands->");
		
		num1=sc.nextInt();
		num2=sc.nextInt();
		
		byte[] n1=(String.valueOf(num1)+" "+String.valueOf(num2)+" "+String.valueOf(op)).getBytes();
	//	byte[] n2=String.valueOf(num2).getBytes();
	//	byte[] opn=String.valueOf(op).getBytes();
		
		InetAddress id=InetAddress.getLocalHost();
		DatagramPacket dp,np1,np2,opp;
		
		dp=new DatagramPacket(b,b.length,id,321);
		ds.send(dp);
		
		np1=new DatagramPacket(n1,n1.length,id,321);
		ds.send(np1);
	/*	
		np2=new DatagramPacket(n1,n2.length,id,321);
		ds.send(np2);
		
		opp=new DatagramPacket(opn,opn.length,id,321);
		ds.send(opp);
	*/	
		
		
		
		byte[] b1=new byte[1024];
		byte[] b2=new byte[1024];
		DatagramPacket dp1,dp2;
		
		dp1=new DatagramPacket(b1,b1.length);
		ds.receive(dp1);
		
		dp2=new DatagramPacket(b2,b2.length);
		ds.receive(dp2);
		
		String str=new String(dp1.getData(),0,dp1.getLength());
		System.out.println(str);
		
		String str2=new String(dp2.getData(),0,dp2.getLength());
		System.out.println(str2);
		
		sc.close();
		ds.close();
	
	}
}
