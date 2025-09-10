import { Component } from '@angular/core'
import { AsyncPipe, CommonModule } from '@angular/common'
import { BehaviorSubject, map, Observable } from 'rxjs'

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, AsyncPipe],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App {
  private readonly countSubject = new BehaviorSubject<number>(0)

  readonly count$: Observable<number> = this.countSubject.asObservable()
  readonly double$: Observable<number> = this.count$.pipe(map(v => v * 2))

  inc(): void {
    this.countSubject.next(this.countSubject.value + 10)
  }

  dec(): void {
    this.countSubject.next(this.countSubject.value - 10)
  }

  reset(): void {
    this.countSubject.next(0)
  }
}



// import { Component } from '@angular/core'
// import { BehaviorSubject, map, Observable } from 'rxjs'

// @Component({
//   selector: 'app-root',
//   templateUrl: './app.html',
//   styleUrls: ['./app.css']
// })
// export class App {
//   private readonly countSubject = new BehaviorSubject<number>(0)

//   readonly count$: Observable<number> = this.countSubject.asObservable()
//   readonly double$: Observable<number> = this.count$.pipe(map(v => v * 2))

//   inc(): void {
//     this.countSubject.next(this.countSubject.value + 10)
//   }

//   dec(): void {
//     this.countSubject.next(this.countSubject.value - 10)
//   }

//   reset(): void {
//     this.countSubject.next(0)
//   }
// }



// import { Component } from '@angular/core';
// import { BehaviorSubject, map } from 'rxjs';

// @Component({
//   selector: 'app-root',
//   templateUrl: './app.html',
//   styleUrls: ['./app.css']
// })
// export class AppComponent {
//   count$ = new BehaviorSubject<number>(0);
//   double$ = this.count$.pipe(map(v => v * 2));

//   inc() {
//     this.count$.next(this.count$.value + 10);
//   }

//   dec() {
//     this.count$.next(this.count$.value - 10);
//   }

//   reset() {
//     this.count$.next(0);
//   }

//   constructor() {
//     console.log('00000000001:', this.count$);
//     this.double$.subscribe(); 
//   }
// }

