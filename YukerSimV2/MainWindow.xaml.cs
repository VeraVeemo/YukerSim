using System.Windows;
using System.Windows.Controls;

namespace YukerSimV2
{
    public partial class MainWindow : Window
    {
        public static int Clicks = 0;

        private void playSFX(string path, int startTime)
        {
            var sfx = new MediaElement();
            sfx.LoadedBehavior = MediaState.Manual;
            sfx.UnloadedBehavior = MediaState.Manual;
            sfx.Source = new(path, UriKind.Relative);
            sfxs.Children.Add(sfx);
            sfx.Position = TimeSpan.FromMilliseconds(startTime);
            sfx.Play();
            sfx.MediaEnded += (_, _) =>
            {
                sfxs.Children.Remove(sfx);
            };
        }

        public void YukerClick(object sender, RoutedEventArgs e)
        {
            Clicks++;
            playSFX("Assets/squish.wav", 120);
            clickAmount.Content = $"Clicks: {Clicks}";
            yukerImg.Width   = 155;
            yukerImg.Height  = 174;
            Task.Delay(300).ContinueWith(_ =>
            {
                Dispatcher.Invoke(() =>
                {
                    yukerImg.Width  = 182;
                    yukerImg.Height = 201;
                });
            });
        }

        public MainWindow()
        {
            InitializeComponent();
        }
    }
}