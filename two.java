public class MainActivity extends AppCompatActivity {
    private TextView counterText;
    private Button startButton, stopButton;
    private int counter = 0;
    private boolean isRunning = false;
    private Handler handler = new Handler();
    private Runnable runnable;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        counterText = findViewById(R.id.counter);
        startButton = findViewById(R.id.start);
        stopButton = findViewById(R.id.stop);

        runnable = new Runnable() {
            @Override
            public void run() {
                if (isRunning) {
                    counterText.setText(String.valueOf(counter++));
                    handler.postDelayed(this, 1000);
                }
            }
        };

        startButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                isRunning = true;
                handler.post(runnable);
            }
        });

        stopButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                isRunning = false;
            }
        });
    }
}
