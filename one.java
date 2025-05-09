public class MainActivity extends AppCompatActivity {

   
    int[] images = {R.drawable.img1, R.drawable.img2, R.drawable.img3, R.drawable.img4, R.drawable.img5};

   
    Handler handler = new Handler();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button wpButton = findViewById(R.id.button);  
        View wallView = findViewById(R.id.wallView);  

        wpButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                
                final Runnable wallpaperChanger = new Runnable() {
                    @Override
                    public void run() {
                        Random random = new Random();
                        int rNum = random.nextInt(images.length);
                        wallView.setBackground(ContextCompat.getDrawable(getApplicationContext(), images[rNum]));
                        handler.postDelayed(this, 3000);
                    }
                };
               
                handler.post(wallpaperChanger);
            }
        });
    }
}
